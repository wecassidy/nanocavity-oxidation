import pandas as pd
import plotnine as p9

resonance = pd.read_csv("sims/nanobeam_resonance.dat")
q = pd.read_csv("sims/nanobeam_q.dat")
spectrum = pd.read_csv("sims/nanobeam_spectrum.dat")

p9.themes.theme_set(p9.theme_bw(base_family="Fira Sans"))

p = (
    p9.ggplot(resonance.query("Resonance == 1"))
    + p9.aes(x="Oxide thickness (nm)", y="Wavelength (nm)")
    + p9.geom_point()
    + p9.labs(title="Nanobeam cavity highest resonance wavelength vs oxide thickness")
)
# p.draw()
p.save("nanobeam_resonance.png")

p = (
    p9.ggplot(
        spectrum[spectrum["Oxide thickness (nm)"].isin((0, 15, 20))].query(
            "`Wavelength (nm)` < 2200"
        )
    )
    + p9.aes(
        x="Wavelength (nm)",
        y="Spectrum (a.u.)",
        color="Oxide thickness (nm)",
        group="Oxide thickness (nm)",
    )
    + p9.geom_line()
    + p9.scale_y_log10()
    + p9.labs(title="Nanobeam cavity spectrum vs oxide thickness")
)
# p.draw()
p.save("nanobeam_spectrum.png")

p = (
    p
    + p9.xlim(1500, 1650)
    + p9.labs(title="Nanobeam cavity highest resonance spectrum")
)
p.save("nanobeam_spectrum_zoom.png")
# p.draw()

p = (
    p9.ggplot(q.query("Resonance == 1"))
    + p9.aes(x="Oxide thickness (nm)", y="Q")
    + p9.geom_point()
    + p9.scale_y_log10()
    + p9.labs(title="Nanobeam cavity highest resonance Q factor vs oxide thickness")
)
p.save("nanobeam_q.png")
p.draw(show=True)
