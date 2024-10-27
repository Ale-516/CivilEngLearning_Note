import plotly
import pyearthquake as eq
my_GM = eq.Motion("GMs","H-E12140",damping = 0.05)
my_GM.load_peer("H-E12140.AT2")
my_GM.convert_peer("H-E12140.AT2")
my_GM.write_accel("acceleration.csv", time = True)
my_GM.write_info("information.csv")
my_GM.write_spectrum("spectrum")
my_GM.plot(folder = "figures", save = True, engine = 'plotly')
a = my_GM.get_duration
print(a)