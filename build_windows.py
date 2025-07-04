BUILD_ALL        = True
BUILD_SPECIFIC   = 'cu128' # Does nothing if BUILD_ALL = True
ZIP_RESULTS      = False
REQUIREMENTS     = 'requirements.txt'
BUILD_PATH       = 'build'

TORCH_VERSIONS = [
    'cpu',
    'cu118',
    'cu126',
    'cu128'
]

import os
import subprocess
import sys

def main():
    venv_path = '.venv'

    os.system(f'uv venv {venv_path}')

    for t_ver in TORCH_VERSIONS if BUILD_ALL else [BUILD_SPECIFIC]:
        if t_ver == 'cpu':
            pip_torch = 'pip install torch --upgrade --index-url https://download.pytorch.org/whl/cpu'
        else:
            pip_torch = f'pip install torch --upgrade --index-url https://download.pytorch.org/whl/{t_ver}'

        cmd = (
            f'cmd.exe /c ".venv\\Scripts\\activate && '
            f'pip install uv && '
            f'uv add -r {REQUIREMENTS} && '
            f'uv run python -m pip uninstall -y torch && '
            f'{pip_torch} && '
            f'uv run spacy download en_core_web_sm && '
            f'python -m PyInstaller KokoroTTSGenerator.spec -y --clean"'
        )

        subprocess.run(cmd, shell=True, check=True)

        dist_dir = os.path.join(os.getcwd(), 'dist')
        final_dir = os.path.join(os.getcwd(), 'Final')
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)

        exported_folder_name = 'KokoroTTSGenerator'
        src_folder = os.path.join(dist_dir, exported_folder_name)

        t_ver_suffix = t_ver if t_ver else 'all'
        dst_folder = os.path.join(final_dir, f'{exported_folder_name}_{t_ver_suffix}')

        if os.path.exists(dst_folder):
            if os.path.isdir(dst_folder):
                import shutil
                shutil.rmtree(dst_folder)
            else:
                os.remove(dst_folder)

        if os.path.exists(src_folder):
            import shutil
            shutil.move(src_folder, dst_folder)

        if not BUILD_ALL:
            break


if __name__ == '__main__':
    main()
