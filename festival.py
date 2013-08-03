import umarutils as u

def txt2wav(s,fn,voice):
    d = "/home/umar/"
    u.writefile(s,d+fn)
    voices(voice)
    u.shellcommand(["text2wave",
                    "-eval",d+"festoptions",
                    d+fn,"-o",d+fn+".wav"])

def voices(v):
    a = [["cmu_us_awb_arctic","awb"],
         ["cmu_us_ksp_arctic","ksp"],
         ["cmu_us_bdl_arctic","bdl"],
         ["cmu_us_rms_arctic","rms"],
         ["cmu_us_clb_arctic","clb"],
         ["cmu_us_slt_arctic","slt"]]
    b = "".join(["(set! voice_default 'voice_",
                 [x[0] for x in a if x[1] == v][0],")"])
    u.writefile(b,"/home/umar/festoptions")

