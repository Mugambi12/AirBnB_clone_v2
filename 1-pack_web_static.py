import subprocess

def run_fabric_script():
    try:
        result = subprocess.run(['fab', '-f', '1-pack_web_static.py', 'do_pack'], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

run_fabric_script()
