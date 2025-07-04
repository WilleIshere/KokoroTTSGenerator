import logging
from src.tts import Pipeline

# Set up logging for this module
logger = logging.getLogger(__name__)

class App():
    """
    Main application class for the Kokoro TTS Generator GUI.
    Handles UI construction, user interaction, and communication with the TTS pipeline.
    """

    def __init__(self):
        """
        Initialize the App, configure the UI theme, static file serving, and prepare UI elements.
        """
        self.pipeline = None
        logger.info("App initialized.")

        from nicegui import ui
        import asyncio
        self.ui = ui
        self.asyncio = asyncio
        self.ui.dark_mode().enable()

        # Serve final_audio directory as static files
        from nicegui import app
        app.native.settings['ALLOW_DOWNLOADS'] = True

        import os
        app.add_static_files('/final_audio', os.path.join(os.getcwd(), 'final_audio'))

        # Refined color theme classes
        self.nightly_primary = 'blue-400'
        self.nightly_accent = 'blue-300'
        logger.info("NiceGUI UI and static files configured.")
        self.nightly_bg = 'bg-gray-950'
        self.nightly_card = 'bg-gray-900'
        self.nightly_text = 'text-blue-400'
        self.nightly_text_secondary = 'text-gray-300'
        self.nightly_label = 'text-blue-300'
        self.nightly_button = 'color=blue outline'
        self.nightly_button_main = 'color=blue unelevated'

        self.pipeline_loaded = False  # Track pipeline state

        self.voices = [
                "af_alloy",
                "af_aoede",
                "af_bella",
                "af_jessica",
                "af_kore",
                "af_nicole",
                "af_nova",
                "af_river",
                "af_sarah",
                "af_sky",
                "am_adam",
                "am_echo",
                "am_eric",
                "am_fenrir",
                "am_liam",
                "am_michael",
                "am_onyx",
                "am_puck",
                "am_santa",
                "af_heart",
            ]

        # --- Begin: Themed background ---
        # Lightweight static SVG background for performance and style
        self.bg_html = self.ui.html(
            '''
            <svg id="kokoro-bg" style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:-1;pointer-events:none;" viewBox="0 0 1920 1080" preserveAspectRatio="none">
                <defs>
                    <radialGradient id="mainBg" cx="60%" cy="40%" r="1.2">
                        <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.22"/>
                        <stop offset="60%" stop-color="#1e293b" stop-opacity="0.98"/>
                        <stop offset="100%" stop-color="#0a101a" stop-opacity="1"/>
                    </radialGradient>
                    <linearGradient id="blueAccent" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#60a5fa" stop-opacity="0.13"/>
                        <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.07"/>
                    </linearGradient>
                    <linearGradient id="grayAccent" x1="1" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="#64748b" stop-opacity="0.07"/>
                        <stop offset="100%" stop-color="#1e293b" stop-opacity="0.10"/>
                    </linearGradient>
                </defs>
                <!-- Main background -->
                <rect width="1920" height="1080" fill="url(#mainBg)"/>
                <!-- Themed geometric shapes (blue and gray) -->
                <ellipse cx="1500" cy="320" rx="420" ry="160" fill="url(#blueAccent)"/>
                <ellipse cx="420" cy="900" rx="340" ry="120" fill="url(#grayAccent)"/>
                <!-- Subtle blue circles for depth -->
                <circle cx="1200" cy="900" r="90" fill="#60a5fa" fill-opacity="0.07"/>
                <circle cx="700" cy="200" r="70" fill="#3b82f6" fill-opacity="0.05"/>
                <!-- Subtle gray circle for depth -->
                <circle cx="300" cy="300" r="110" fill="#1e293b" fill-opacity="0.07"/>
                <!-- Soft vignette overlay -->
                <radialGradient id="vignette" cx="50%" cy="50%" r="0.9">
                    <stop offset="70%" stop-color="white" stop-opacity="0"/>
                    <stop offset="100%" stop-color="#0a101a" stop-opacity="0.70"/>
                </radialGradient>
                <rect width="1920" height="1080" fill="url(#vignette)"/>
            </svg>
            '''
        )
        # --- End: Themed background ---

        # Create improved loading dialog
        self.loading_dialog = self.ui.dialog().props('persistent').classes('flex items-center justify-center')
        with self.loading_dialog:
            with self.ui.card().classes('p-8 rounded-2xl shadow-2xl bg-gradient-to-br from-blue-950/90 to-blue-900/80 border border-blue-700/60 backdrop-blur-xl max-w-md w-full flex flex-col items-center'):
                # Animated SVG or Lottie loader (fallback to spinner if not available)
                self.ui.html('''
                    <svg width="64" height="64" viewBox="0 0 64 64" class="kokoro-loader mb-4" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="32" cy="32" r="28" stroke="#3b82f6" stroke-width="6" opacity="0.18"/>
                        <circle cx="32" cy="32" r="22" stroke="#60a5fa" stroke-width="4" stroke-linecap="round"
                            stroke-dasharray="34 100" stroke-dashoffset="0">
                            <animateTransform attributeName="transform" type="rotate" from="0 32 32" to="360 32 32" dur="1.2s" repeatCount="indefinite"/>
                        </circle>
                        <circle cx="32" cy="32" r="14" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"
                            stroke-dasharray="18 60" stroke-dashoffset="0">
                            <animateTransform attributeName="transform" type="rotate" from="360 32 32" to="0 32 32" dur="1.8s" repeatCount="indefinite"/>
                        </circle>
                    </svg>
                ''')
                self.loading_label = self.ui.label(
                    'Loading TTS pipeline...'
                ).classes('text-xl text-blue-200 font-bold mb-2 text-center drop-shadow')
                self.loading_sub = self.ui.label(
                    'This may take up to a minute the first time.<br>Please wait while models are loaded and optimized.'
                ).classes('text-base text-blue-300/80 mb-4 text-center').props('v-html')
                # Progress bar (indeterminate, hide value)
                self.loading_progress = self.ui.linear_progress().props('color="blue" indeterminate show-value="false"').classes('w-full mb-2')
                # Optional: fun tip or reassurance
                self.loading_tip = self.ui.label(
                    'Tip: The pipeline only needs to load once per session.'
                ).classes('text-sm text-blue-400/70 mt-2 text-center italic')
                # Subtle animated glow
                self.ui.html('''
                    <style>
                    .kokoro-loader {
                        filter: drop-shadow(0 0 16px #3b82f6cc);
                        margin-bottom: 1.5rem;
                    }
                    .q-dialog__inner {
                        background: transparent !important;
                    }
                    </style>
                ''')

        # Create generate dialog (for showing progress and result)
        self.generate_dialog = self.ui.dialog().props('persistent').classes('flex items-center justify-center')
        with self.generate_dialog:
            with self.ui.card().classes('p-8 rounded-2xl shadow-2xl bg-gradient-to-br from-blue-950/90 to-blue-900/80 border border-blue-700/60 backdrop-blur-xl max-w-md w-full flex flex-col items-center'):
                self.generate_loader_html = self.ui.html('''
                    <svg width="48" height="48" viewBox="0 0 64 64" class="kokoro-loader mb-4" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="32" cy="32" r="22" stroke="#60a5fa" stroke-width="4" stroke-linecap="round"
                            stroke-dasharray="34 100" stroke-dashoffset="0">
                            <animateTransform attributeName="transform" type="rotate" from="0 32 32" to="360 32 32" dur="1.2s" repeatCount="indefinite"/>
                        </circle>
                    </svg>
                ''')
                self.generate_label = self.ui.label(
                    'Generating audio...'
                ).classes('text-xl text-blue-200 font-bold mb-2 text-center drop-shadow')
                self.generate_progress = self.ui.linear_progress().props('color="blue" indeterminate show-value="false"').classes('w-full mb-2')
                self.generate_result_area = self.ui.column().classes('w-full items-center justify-center mt-4').style('display:none;')
                # Will be filled in after generation

                # --- Add: persistent audio player and download/close buttons ---
                self.preview_label = self.ui.label('Preview:').classes('text-blue-200 font-semibold mb-2').style('display:none;')
                self.audio_player = self.ui.audio('').props('controls').classes('w-full mb-2').style('display:none;')
                self.download_btn = self.ui.button('Download', icon='download').props('color=blue outline').classes('mt-2').style('display:none;')
                self.close_btn = self.ui.button('Close', icon='close').props('color=grey outline').classes('mt-2').style('display:none;')

        self.construct_ui()
        # Hide progress bar value globally to remove '0' from all progress bars
        self.ui.html("""
        <style>
        .q-linear-progress__value {
            display: none !important;
        }
        </style>
        """)

        import os
        os.environ["PYWEBVIEW_GUI"] = "qt"
        os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-gpu --ignore-gpu-blocklist"

        # Get screen size using screeninfo
        try:
            from screeninfo import get_monitors
            monitor = get_monitors()[0]
            screen_width = monitor.width
            screen_height = monitor.height
        except Exception as e:
            logger.warning(f"Could not get screen size, using default 1280x800. Error: {e}")
            screen_width = 1280
            screen_height = 800

        self.ui.run(
            reload=False,
            show=True,
            title='Kokoro TTS Generator',
            dark=True,
            native=True,
            window_size=(screen_width, screen_height)
        )

    def construct_ui(self):
        """
        Build the main user interface for the TTS generator, including all controls and dialogs.
        """
        logger.info("Constructing main UI.")
        ui = self.ui  # Local alias for readability

        # Refined card and layout classes for a modern, clean look
        card_classes = (
            f'w-full max-w-2xl mx-auto mt-24 p-10 shadow-2xl rounded-2xl border border-blue-900/40 {self.nightly_card} backdrop-blur-md'
        )
        title_classes = f'text-4xl font-extrabold text-center tracking-tight {self.nightly_text} mb-2 drop-shadow'
        subtitle_classes = f'text-lg text-center {self.nightly_text_secondary} mb-8'
        settings_label_classes = f'text-xl font-semibold {self.nightly_label} mb-2 mt-6'
        more_label_classes = f'text-lg font-semibold {self.nightly_label} mt-6 mb-2'

        with ui.card().classes(card_classes).style('border: 2px solid #3b82f6;'):
            # Title
            ui.label('Kokoro TTS Generator').classes(title_classes)
            ui.label('High-Quality Local Text-to-Speech').classes(subtitle_classes)

            # Pipeline status and load button
            with ui.row().classes('justify-between items-center mb-6'):
                self.pipeline_status = ui.label(
                    'Pipeline Loaded: No'
                ).classes('text-sm text-red-400 font-semibold transition-all')

                self.load_btn = ui.button(
                    'Load Pipeline'
                ).props(self.nightly_button).classes('ml-auto px-4 py-2 text-base font-semibold rounded-lg shadow-sm transition-all')

            self.warning_label = ui.label(
                '⚠️ Load the pipeline before generating audio. First load may take up to a minute.'
            ).classes('text-sm text-yellow-300 mb-4 font-semibold text-center w-full')

            ui.separator().classes('my-4 opacity-60')

            # Settings section
            ui.label('Settings').classes(settings_label_classes)
            with ui.row().classes('items-center mb-4 gap-4 justify-center'):
                self.voice_label = ui.label('Voice:').classes('mr-2 text-blue-200 font-semibold')
                self.voice_select = ui.select(
                    self.voices,
                    value=self.voices[1] if self.voices else None
                ).classes(
                    'w-44 bg-blue-950/80 text-blue-300 border-2 border-blue-700 focus:border-blue-400 rounded-lg shadow-inner transition-all'
                ).props('outlined dense color="blue"')

            self.input_label = ui.label('Input text (max 2500 chars):').classes('mb-1 text-blue-200 font-semibold')
            self.textarea = ui.textarea().props('outlined').classes(
                'w-full mb-6 bg-blue-950/80 text-blue-100 border-2 border-blue-700 focus:border-blue-400 rounded-xl shadow-inner font-mono transition-all'
            ).style('min-height: 6em;')

            # More section
            ui.label('More').classes(more_label_classes)

            # Speed slider
            with ui.row().classes('items-center mb-3 gap-4 justify-center'):
                self.speed_label = ui.label('Speed:').classes('mr-2 text-blue-200 font-semibold')
                self.speed_value = ui.label('1.0x').classes('ml-2 text-blue-300 font-mono')

                def update_speed_label(e):
                    self.speed_value.text = f'{e.value:.1f}x'

                self.speed_slider = ui.slider(
                    min=0.5, max=2, step=0.1, value=1, on_change=update_speed_label
                ).classes(
                    'w-64 q-slider--dark text-blue-400'
                ).props('color="blue" track-color="blue-700" thumb-color="blue-400"')

            # Pitch slider
            with ui.row().classes('items-center mb-6 gap-4 justify-center'):
                self.pitch_label = ui.label('Pitch:').classes('mr-2 text-blue-200 font-semibold')
                self.pitch_value = ui.label(' 0 ').classes('ml-2 text-blue-300 font-mono').style('min-width: 2.5em; display: inline-block; text-align: center;')

                def update_pitch_label(e):
                    val = int(e.value)
                    if val >= 0:
                        self.pitch_value.text = f' {val} '
                    else:
                        self.pitch_value.text = f'{val} '

                self.pitch_slider = ui.slider(
                    min=-10, max=10, step=1, value=0, on_change=update_pitch_label
                ).classes(
                    'w-64 q-slider--dark text-blue-400'
                ).props('color="blue" track-color="blue-700" thumb-color="blue-400"')

            # Generate button - FLAT & MODERN
            self.generate_btn = ui.button(
                '',  # No text, icon only
                icon='graphic_eq'
            ).props(
                'color=blue-4 flat size=xl round'
            ).classes(
                'w-full mt-8 text-xl font-extrabold py-5 rounded-full bg-blue-700 hover:bg-blue-600 active:bg-blue-800 text-white tracking-wide transition-all focus:ring-4 focus:ring-blue-400/40 flex items-center justify-center group shadow-none border-none'
            )
            self.generate_btn.tooltip(
                'Generate audio (You must load the pipeline first)'
            )
            # Add a modern animated ripple effect using HTML/CSS (no pulse, more flat)
            self.ui.html(
                '''
                <style>
                .kokoro-generate-btn .q-icon {
                    font-size: 2.5rem !important;
                    filter: drop-shadow(0 2px 8px #2563eb44);
                    transition: color 0.2s;
                }
                .kokoro-generate-btn:active .q-icon,
                .kokoro-generate-btn:focus .q-icon {
                    color: #fff !important;
                    filter: drop-shadow(0 4px 16px #3b82f6cc);
                }
                .kokoro-generate-btn {
                    position: relative;
                    overflow: hidden;
                }
                .kokoro-generate-btn::after {
                    content: '';
                    position: absolute;
                    left: 50%;
                    top: 50%;
                    width: 0;
                    height: 0;
                    background: rgba(59,130,246,0.18);
                    border-radius: 9999px;
                    transform: translate(-50%,-50%);
                    opacity: 0;
                    transition: width 0.3s, height 0.3s, opacity 0.3s;
                    pointer-events: none;
                }
                .kokoro-generate-btn:active::after {
                    width: 160%;
                    height: 160%;
                    opacity: 1;
                    transition: 0s;
                }
                </style>
                '''
            )
            # Wrap the button in a row for alignment (no pulse div)
            with ui.row().classes('kokoro-generate-btn-wrap').style('position:relative; width:100%;'):
                self.generate_btn.classes('kokoro-generate-btn')

            # Disable all settings and generate button initially
            self.set_controls_enabled(False)

            # Attach load pipeline logic
            self.load_btn.on('click', self.load_pipeline)

            # Attach generate logic
            self.generate_btn.on('click', self.on_generate_clicked)
        logger.info("UI construction complete.")

    async def load_pipeline(self):
        """
        Asynchronously load the TTS pipeline, updating the UI to reflect loading state.
        """
        logger.info("User requested pipeline load.")
        self.load_btn.disable()
        self.pipeline_status.text = 'Pipeline Loading... (this may take up to a minute)'
        self.pipeline_status.classes('text-sm text-yellow-300 font-semibold transition-all')
        self.loading_label.text = 'Loading TTS pipeline...'
        self.loading_sub.text = 'This may take up to a minute the first time.<br>Please wait while models are loaded and optimized.'
        self.loading_progress.visible = True
        self.loading_dialog.open()

        self.pipeline = Pipeline()
        await self.asyncio.to_thread(self.pipeline.load)

        self.pipeline_loaded = True
        self.pipeline_status.text = 'Pipeline Loaded: Yes'
        self.pipeline_status.classes('text-sm text-green-400 font-semibold transition-all')
        self.set_controls_enabled(True)
        self.load_btn.disable()  # Optionally keep disabled after loading
        self.loading_progress.visible = False
        self.loading_dialog.close()
        # Remove the warning label if present
        if hasattr(self, 'warning_label'):
            self.warning_label.visible = False
        logger.info("Pipeline loaded and UI updated.")

    async def on_generate_clicked(self):
        """
        Handle the generate button click: validate input, call the TTS pipeline, and update the UI with results.
        """
        logger.info("Generate button clicked.")
        # Only allow if pipeline is loaded
        if not self.pipeline_loaded or not self.pipeline:
            logger.warning("Generate attempted before pipeline loaded.")
            return

        # Get input values
        text = self.textarea.value or ""
        voice = self.voice_select.value
        speed = self.speed_slider.value
        pitch = self.pitch_slider.value

        # Validate input
        if not text.strip():
            self.ui.notify('Please enter text to synthesize.', color='warning')
            logger.warning("No text entered for synthesis.")
            return

        # Show generate dialog, reset result area
        self.generate_label.text = 'Generating audio...'
        self.generate_progress.visible = True
        self.generate_result_area.style('display:none;')
        self.generate_loader_html.style('display:block;')
        self.preview_label.style('display:none;')
        self.audio_player.style('display:none;')
        self.download_btn.style('display:none;')
        self.close_btn.style('display:none;')
        self.generate_dialog.open()

        # Wait for the generation to finish before allowing further actions
        self.generate_btn.disable()
        self.set_controls_enabled(False)
        try:
            filepath = await self.asyncio.to_thread(
                self.pipeline.generate,
                text,
                voice,
                speed,
                pitch
            )
        except Exception as e:
            self.generate_dialog.close()
            self.ui.notify(f'Error during generation: {e}', color='negative')
            logger.error(f"Error during audio generation: {e}")
            self.generate_btn.enable()
            self.set_controls_enabled(True)
            return

        self.generate_btn.enable()
        self.set_controls_enabled(True)

        # --- Show preview and download dialog after generation ---
        if filepath:
            # Set up preview and download controls
            from urllib.parse import quote
            filename = filepath.split('/')[-1]
            url = f'/final_audio/{quote(filename)}'

            self.generate_label.text = 'Audio generated!'
            self.generate_progress.visible = False
            self.generate_loader_html.style('display:none;')
            self.preview_label.style('display:block;')
            self.audio_player.props(f'controls src="{url}"')
            self.audio_player.style('display:block;')
            self.download_btn.style('display:block;')
            self.download_btn.on('click', lambda: self._download_file(url, filename))
            self.close_btn.style('display:block;')
            self.close_btn.on('click', lambda: self.generate_dialog.close())

            self.generate_result_area.style('display:flex;')
            logger.info(f"Audio generated successfully: {filepath}")
        else:
            self.generate_loader_html.style('display:none;')
            self.generate_dialog.close()
            self.ui.notify('No audio was generated.', color='warning')
            logger.warning("No audio was generated.")

    def set_controls_enabled(self, enabled: bool):
        """
        Enable or disable all user controls in the UI.

        Args:
            enabled (bool): Whether to enable (True) or disable (False) the controls.
        """
        logger.debug(f"Setting controls enabled: {enabled}")
        # Enable/disable all settings and generate button
        for ctrl in [
            self.voice_select,
            self.textarea,
            self.speed_slider,
            self.pitch_slider,
            self.generate_btn,
        ]:
            if enabled:
                ctrl.enable()
            else:
                ctrl.disable()
        # Hide preview label and audio player when controls are disabled (i.e., before generation)
        if not enabled:
            self.preview_label.style('display:none;')
            self.audio_player.style('display:none;')

    def _download_file(self, url, filename):
        """
        Helper to trigger browser download using a hidden anchor tag with the download attribute.
        """
        # Remove any previous download link if present
        self.ui.run_javascript('''
            var old = document.getElementById("kokoro-download-link");
            if (old) old.remove();
        ''')
        # Create and click a new download link
        self.ui.run_javascript(f'''
            var a = document.createElement("a");
            a.id = "kokoro-download-link";
            a.href = "{url}";
            a.download = "{filename}";
            a.style.display = "none";
            document.body.appendChild(a);
            a.click();
            setTimeout(function() {{
                a.remove();
            }}, 1000);
        ''')
