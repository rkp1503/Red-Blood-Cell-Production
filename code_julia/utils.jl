#=============================================================================
Author: Ramsey (Rayla) Phuc
Alias: Rayla Kurosaki
GitHub: https://github.com/rkp1503
Project: Red Blood Cell Production
=============================================================================#

module utils
import Plots: plot, plot!

    function myPlot(tₘₐₓ, t_arr, R_arr, γ_colors, filename, normalize=1)
        figure = Plots.plot(
            title="Red Blood Cell Population over $tₘₐₓ Days",
            xaxis="Time in days",
            yaxis="Red Blood Cell Population",

            # legend=:outertopright, 
            background_color_inside="#DDDDDD", 
            gridalpha=1,
            gridlinewidth=:1,
            foreground_color_grid="#000000",
            minorgrid=true,
            minorgridalpha=0.5,
            foreground_color_minor_grid=:"#FF0000",
            
            # gridalpha=0,
            )
        for (tₛ, Rₛ, γ_color) in zip(t_arr, R_arr, γ_colors)
            label, color = γ_color
            Plots.plot!(
                figure, tₛ, Rₛ/normalize, label="γ=$label", linecolor=color, 
                linewidth=2
                )
        end
        return figure
    end;

end
