#=============================================================================
Author: Ramsey (Rayla) Phuc
Alias: Rayla Kurosaki
GitHub: https://github.com/rkp1503
Project: Red Blood Cell Production
=============================================================================#

module utils
    using Plots

    export myPlot
    function myPlot(tₘₐₓ, t_arr, R_arr, γₛ, colors, filename, normalize=1)
        figure = Plots.plot(
            title="Red Blood Cell Population over $tₘₐₓ Days", 
            xaxis="Time in days", 
            yaxis="Red Blood Cell Population", 
            legend=:outertopright,  
            foreground_color_grid="#000000", 
            gridalpha=1, 
            gridlinewidth=:1.5, 
            minorgrid=true, 
            foreground_color_minor_grid=:"#FF0000", 
            minorgridalpha=0.75
            )
        for (tₛ, Rₛ, label, color) in zip(t_arr, R_arr, γₛ, colors)
            Plots.plot!(
                figure, tₛ, Rₛ/normalize, label=label, linecolor=color, 
                linewidth=2
                )
        end
        return figure
    end;
end
