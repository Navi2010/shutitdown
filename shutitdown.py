import os
import platform

def shutdown():
    system_name = platform.system()

    if system_name == 'Windows':
        os.system('shutdown /s /t 1')
    elif system_name in ('Linux', 'Darwin'):
        os.system('sudo shutdown now')
    else:
        print('unsupported system')

def main():
    print('shutting down system: ')
    shutdown()

if __name__ == "__main__":
    main()