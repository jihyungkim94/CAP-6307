from pyrouge import Rouge155

import glob

r = Rouge155()

for system in glob.glob("System_Summaries/Centroid/"):
    r.system_dir = system
    r.system_filename_pattern = "d(\d+)t.[A-Za-z]+"

    r.model_dir = "Human_Summaries/eval/"
    r.model_filename_pattern = "D#ID#.M.100.T.[A-Z]"


    output = r.convert_and_evaluate()

    print("RESULTS FOR {}".format(system))
    print(output)

for system in glob.glob("System_Summaries/DPP/"):
    r.system_dir = system
    r.system_filename_pattern = "d(\d+)t.[A-Za-z]+"

    r.model_dir = "Human_Summaries/eval/"
    r.model_filename_pattern = "D#ID#.M.100.T.[A-Z]"


    output = r.convert_and_evaluate()


    print("RESULTS FOR {}".format(system))
    print(output)

for system in glob.glob("System_Summaries/ICSISumm/"):
    r.system_dir = system
    r.system_filename_pattern = "d(\d+)t.[A-Za-z]+"

    r.model_dir = "Human_Summaries/eval/"
    r.model_filename_pattern = "D#ID#.M.100.T.[A-Z]"

    output = r.convert_and_evaluate()


    print("RESULTS FOR {}".format(system))
    print(output)


for system in glob.glob("System_Summaries/LexRank/"):
    r.system_dir = system
    r.system_filename_pattern = "d(\d+)t.[A-Za-z]+"

    r.model_dir = "Human_Summaries/eval/"
    r.model_filename_pattern = "D#ID#.M.100.T.[A-Z]"

    output = r.convert_and_evaluate()

    print("RESULTS FOR {}".format(system))
    print(output)


for system in glob.glob("System_Summaries/Submodular/"):
    r.system_dir = system
    r.system_filename_pattern = "d(\d+)t.[A-Za-z]+"

    r.model_dir = "Human_Summaries/eval/"
    r.model_filename_pattern = "D#ID#.M.100.T.[A-Z]"

    output = r.convert_and_evaluate()

    print("RESULTS FOR {}".format(system))
    print(output)



