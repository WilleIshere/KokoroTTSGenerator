import logging
from src.tts import Pipeline

# Set up logging for this module
logger = logging.getLogger(__name__)

class App():
    def __init__(self):
        self.pipeline = None
        logger.info("App initialized.")

        from nicegui import ui
        import asyncio
        self.ui = ui
        self.asyncio = asyncio
        self.ui.dark_mode().enable()

        # Serve final_audio directory as static files
        from nicegui import app
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
        # A fixed SVG background using only the app's blue and gray palette, with subtle animated gradients and geometric shapes
        self.bg_html = self.ui.html(
            '''
            <svg id="kokoro-bg" style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:-1;pointer-events:none;" viewBox="0 0 1920 1080" preserveAspectRatio="none">
                <defs>
                    <!-- Main radial gradient for background -->
                    <radialGradient id="mainBg" cx="60%" cy="40%" r="1.2">
                        <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.22">
                            <animate attributeName="stop-opacity" values="0.22;0.32;0.22" dur="10s" repeatCount="indefinite"/>
                        </stop>
                        <stop offset="60%" stop-color="#1e293b" stop-opacity="0.98"/>
                        <stop offset="100%" stop-color="#0a101a" stop-opacity="1"/>
                    </radialGradient>
                    <!-- Blue accent gradient for geometric shapes -->
                    <linearGradient id="blueAccent" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#60a5fa" stop-opacity="0.13"/>
                        <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.07"/>
                    </linearGradient>
                    <!-- Gray accent gradient for geometric shapes -->
                    <linearGradient id="grayAccent" x1="1" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="#64748b" stop-opacity="0.07"/>
                        <stop offset="100%" stop-color="#1e293b" stop-opacity="0.10"/>
                    </linearGradient>
                    <!-- Aurora gradient for animated overlay -->
                    <linearGradient id="aurora1" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#a5b4fc" stop-opacity="0.13"/>
                        <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.10"/>
                        <stop offset="100%" stop-color="#818cf8" stop-opacity="0.13"/>
                    </linearGradient>
                    <linearGradient id="aurora2" x1="1" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="#f472b6" stop-opacity="0.10"/>
                        <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.08"/>
                    </linearGradient>
                    <filter id="blur1" x="-20%" y="-20%" width="140%" height="140%">
                        <feGaussianBlur stdDeviation="60"/>
                    </filter>
                    <filter id="blur2" x="-20%" y="-20%" width="140%" height="140%">
                        <feGaussianBlur stdDeviation="90"/>
                    </filter>
                    <filter id="blurAurora" x="-30%" y="-30%" width="160%" height="160%">
                        <feGaussianBlur stdDeviation="120"/>
                    </filter>
                </defs>
                <!-- Main background -->
                <rect width="1920" height="1080" fill="url(#mainBg)"/>
                <!-- Themed geometric shapes (blue and gray) -->
                <ellipse cx="1500" cy="320" rx="420" ry="160" fill="url(#blueAccent)" filter="url(#blur1)">
                    <animate attributeName="rx" values="420;480;420" dur="16s" repeatCount="indefinite"/>
                    <animate attributeName="ry" values="160;200;160" dur="16s" repeatCount="indefinite"/>
                    <animate attributeName="cx" values="1500;1400;1500" dur="20s" repeatCount="indefinite"/>
                </ellipse>
                <ellipse cx="420" cy="900" rx="340" ry="120" fill="url(#grayAccent)" filter="url(#blur2)">
                    <animate attributeName="cx" values="420;520;420" dur="18s" repeatCount="indefinite"/>
                    <animate attributeName="rx" values="340;370;340" dur="15s" repeatCount="indefinite"/>
                </ellipse>
                <!-- Subtle blue circles for depth -->
                <circle cx="1200" cy="900" r="90" fill="#60a5fa" fill-opacity="0.07">
                    <animate attributeName="cy" values="900;950;900" dur="13s" repeatCount="indefinite"/>
                    <animate attributeName="r" values="90;110;90" dur="15s" repeatCount="indefinite"/>
                </circle>
                <circle cx="700" cy="200" r="70" fill="#3b82f6" fill-opacity="0.05">
                    <animate attributeName="cx" values="700;800;700" dur="17s" repeatCount="indefinite"/>
                    <animate attributeName="r" values="70;90;70" dur="14s" repeatCount="indefinite"/>
                </circle>
                <!-- Subtle gray circle for depth -->
                <circle cx="300" cy="300" r="110" fill="#1e293b" fill-opacity="0.07">
                    <animate attributeName="cy" values="300;350;300" dur="19s" repeatCount="indefinite"/>
                    <animate attributeName="r" values="110;130;110" dur="17s" repeatCount="indefinite"/>
                </circle>
                <!-- Animated Aurora/Wave overlays -->
                <path id="aurora1" d="M0,700 Q600,600 1200,800 T1920,700 V1080 H0Z"
                    fill="url(#aurora1)" filter="url(#blurAurora)" opacity="0.5">
                    <animate attributeName="d"
                        values="
                            M0,700 Q600,600 1200,800 T1920,700 V1080 H0Z;
                            M0,720 Q700,650 1300,850 T1920,720 V1080 H0Z;
                            M0,700 Q600,600 1200,800 T1920,700 V1080 H0Z
                        "
                        dur="18s" repeatCount="indefinite"/>
                    <animate attributeName="opacity"
                        values="0.5;0.7;0.5"
                        dur="18s" repeatCount="indefinite"/>
                </path>
                <path id="aurora2" d="M0,800 Q900,950 1920,850 V1080 H0Z"
                    fill="url(#aurora2)" filter="url(#blurAurora)" opacity="0.35">
                    <animate attributeName="d"
                        values="
                            M0,800 Q900,950 1920,850 V1080 H0Z;
                            M0,820 Q1000,900 1920,870 V1080 H0Z;
                            M0,800 Q900,950 1920,850 V1080 H0Z
                        "
                        dur="22s" repeatCount="indefinite"/>
                    <animate attributeName="opacity"
                        values="0.35;0.55;0.35"
                        dur="22s" repeatCount="indefinite"/>
                </path>
                <!-- Faint animated grid overlay -->
                <g opacity="0.07">
                    <g>
                        <rect x="0" y="0" width="1920" height="1080" fill="none" stroke="#60a5fa" stroke-width="1"/>
                        <g>
                            <g>
                                <line x1="0" y1="180" x2="1920" y2="180" stroke="#60a5fa">
                                    <animate attributeName="y1" values="180;200;180" dur="16s" repeatCount="indefinite"/>
                                    <animate attributeName="y2" values="180;200;180" dur="16s" repeatCount="indefinite"/>
                                </line>
                                <line x1="0" y1="360" x2="1920" y2="360" stroke="#60a5fa">
                                    <animate attributeName="y1" values="360;380;360" dur="18s" repeatCount="indefinite"/>
                                    <animate attributeName="y2" values="360;380;360" dur="18s" repeatCount="indefinite"/>
                                </line>
                                <line x1="0" y1="540" x2="1920" y2="540" stroke="#60a5fa">
                                    <animate attributeName="y1" values="540;560;540" dur="20s" repeatCount="indefinite"/>
                                    <animate attributeName="y2" values="540;560;540" dur="20s" repeatCount="indefinite"/>
                                </line>
                                <line x1="0" y1="720" x2="1920" y2="720" stroke="#60a5fa">
                                    <animate attributeName="y1" values="720;740;720" dur="22s" repeatCount="indefinite"/>
                                    <animate attributeName="y2" values="720;740;720" dur="22s" repeatCount="indefinite"/>
                                </line>
                                <line x1="0" y1="900" x2="1920" y2="900" stroke="#60a5fa">
                                    <animate attributeName="y1" values="900;920;900" dur="24s" repeatCount="indefinite"/>
                                    <animate attributeName="y2" values="900;920;900" dur="24s" repeatCount="indefinite"/>
                                </line>
                            </g>
                            <g>
                                <line y1="0" x1="320" y2="1080" x2="320" stroke="#60a5fa">
                                    <animate attributeName="x1" values="320;340;320" dur="17s" repeatCount="indefinite"/>
                                    <animate attributeName="x2" values="320;340;320" dur="17s" repeatCount="indefinite"/>
                                </line>
                                <line y1="0" x1="640" y2="1080" x2="640" stroke="#60a5fa">
                                    <animate attributeName="x1" values="640;660;640" dur="19s" repeatCount="indefinite"/>
                                    <animate attributeName="x2" values="640;660;640" dur="19s" repeatCount="indefinite"/>
                                </line>
                                <line y1="0" x1="960" y2="1080" x2="960" stroke="#60a5fa">
                                    <animate attributeName="x1" values="960;980;960" dur="21s" repeatCount="indefinite"/>
                                    <animate attributeName="x2" values="960;980;960" dur="21s" repeatCount="indefinite"/>
                                </line>
                                <line y1="0" x1="1280" y2="1080" x2="1280" stroke="#60a5fa">
                                    <animate attributeName="x1" values="1280;1300;1280" dur="23s" repeatCount="indefinite"/>
                                    <animate attributeName="x2" values="1280;1300;1280" dur="23s" repeatCount="indefinite"/>
                                </line>
                                <line y1="0" x1="1600" y2="1080" x2="1600" stroke="#60a5fa">
                                    <animate attributeName="x1" values="1600;1620;1600" dur="25s" repeatCount="indefinite"/>
                                    <animate attributeName="x2" values="1600;1620;1600" dur="25s" repeatCount="indefinite"/>
                                </line>
                            </g>
                        </g>
                    </g>
                </g>
                <!-- Soft overlay for vignette effect -->
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
        self.ui.run(reload=False, show=True)

    def construct_ui(self):
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

    async def load_pipeline(self):
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

    async def on_generate_clicked(self):
        # Only allow if pipeline is loaded
        if not self.pipeline_loaded or not self.pipeline:
            return

        # Get input values
        text = self.textarea.value or ""
        voice = self.voice_select.value
        speed = self.speed_slider.value
        pitch = self.pitch_slider.value

        # Validate input
        if not text.strip():
            self.ui.notify('Please enter text to synthesize.', color='warning')
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
            self.download_btn.on('click', lambda: self.ui.open(url))
            self.close_btn.style('display:block;')
            self.close_btn.on('click', lambda: self.generate_dialog.close())

            self.generate_result_area.style('display:flex;')
        else:
            self.generate_loader_html.style('display:none;')
            self.generate_dialog.close()
            self.ui.notify('No audio was generated.', color='warning')

    def set_controls_enabled(self, enabled: bool):
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
