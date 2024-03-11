import os
import yaml




def versioning(file_path="secrets.yml"):
    # TODO: if SERVICES-secrets.yml already exists, ask user to Overwrite/Rename/Both [O/r/b] - default is Overwrite. Accourding to the user's input overwrite the existing file, rename the new file (if new_name contains '/' a new directory will be created) or keep both which adds a suffix "-v-"+major_index+"."+minor_index to the new yml file - index is an integer, if the existing file already ends with f.e. -v-1.0 major_index is equal to 1, or major_index is 2 if the exististing file ends with something like -v-2.4 - the minor_index is always +1 from the existing file's minor_index
    pass

def maj_min_index(suffix='-v-0.0'):
    init_sfx = "-v-0.0"
    major_index = suffix.split('.')[-2].replace('-v-')
    minor_index = suffix.split('.')[-1]
    return major_index, minor_index

def version_suffix(old_file="secrets-v-0.0.yml", new_file="secrets-v-0.1.yml"):
    old_sfx = old_file.split('/')[:-1] if '/' in old_file else old_file
    old_sfx = old_file.replace('.yml', '')
    old_sfx = old_file.replace('.yaml', '')
    old_sfx = old_file[:-6]
    old_maj_index, old_min_index = maj_min_index(old_sfx)
    new_sfx = new_file.split('/')[:-1] if '/' in new_file else new_file
    new_sfx = old_file.replace('.yml', '')
    new_sfx = old_file.replace('.yaml', '')
    new_sfx = new_file[:-6]
    new_maj_index, new_min_index = maj_min_index(new_sfx)
    new_min_index = new_min_index if new_min_index > old_min_index else new_min_index+1
    new_maj_index = old_maj_index
    old_sfx = f"-v-{old_maj_index}.{old_min_index}"
    new_sfx = f"-v-{new_maj_index}.{new_min_index}"
    return old_sfx, new_sfx

def saving_yml(file_path="secrets.yml", yaml_string=''):
    if '/' not in file_path:
        dir_path = 'auto_generated_YAML'
    else:
        pathparts = file_path.split('/')
        dir_path = ''
        for dirname in pathparts[:-2]:
            # TODO: mkdir dirname
            dir_path += dirname
    existing_file_list = os.listdir(dir_path)
    for existing_file in existing_file_list:
        existing_file = existing_file if '/' in existing_file else os.path.join(dir_path, existing_file)
        if os.abspath(file_path) == os.abspath(existing_file):
            user_choice = input("File already exists - Overwrite/Rename/Both [O/r/b]")
            if user_choice.lower() == 'r':
                new_name = input("Please change the file name or file path:")
                while new_name in existing_file_list:
                    last_name = new_name
                    new_name = input("File already existing! Please change file name / hit 'w' for overwrite / hit 'enter' with an empty input for updating version index:")
                    if new_name.lower() == 'w':
                        with open(new_name, 'w') as new_file:
                            yaml.dump(yaml_string, new_file)
                        return f"File saved in {new_name}"
                    elif new_name.len() == 0 or new_file == '':
                        major_index, minor_index = maj_min_index(last_name)
                        major_index += 1 
                        minor_index = 1
                        suffix = f"-v-{major_index}.{minor_index}.yml"
                        new_name = last_name.replace('.yml','')[:-6] + suffix
                        with open(new_name, 'w') as new_file:
                            yaml.dump(yaml_string, new_file)
                        return f"File saved in {new_name}"
                if new_name not in existing_file_list:
                    with open(new_name, 'w') as file:
                        yaml.dump(yaml_string, file)
                        print("File saved in {file_path}")
                    return f"File saved in {new_name}"
                
            


def encode_base64(string):
    pass


def env2secrets(env_file_path=None):
    # TODO: create templates/env_secrets.yml as template how to define k8s secrets in a yml file
    # TODO: generate SERVICE-secrets.yml files for a k8s cluster from .env file
    # TODO: base64 encode each value (=secret) in each line of .env file if the line is not empty and does not start with '#'
    # TODO: if "**secrets.yml" not in .gitignore, add it to the end of the file
    # TODO: add SERVICES-secrets.yml to end of .gitignore file
    # TODO: if SERVICES-secrets.yml already exists, ask user to Overwrite/Rename/Both [O/r/b] - default is Overwrite. Accourding to the user's input overwrite the existing file, rename the new file (if new_name contains '/' a new directory will be created) or keep both which adds a suffix "-v-"+major_index+"."+minor_index to the new yml file - index is an integer, if the existing file already ends with f.e. -v-1.0 major_index is equal to 1, or major_index is 2 if the exististing file ends with something like -v-2.4 - the minor_index is always +1 from the existing file's minor_index
    # TODO: else save SERVICES-secrets.yml 
    # TODO: print statement with clickable SERVICE-secrets.yml path in terminal
    pass



def compose2deployments(docker_compose_file_path=None):
    # TODO: read the docker-compose.yml file in docker_compose_file_path
    # TODO: For each SERVICE create a SERVICE-deployment.yml, a SERVICE-service.yml, a SERVICE-pvc.yml and/or a SERVICE-ingress.yml
    # TODO: 
