#=============================================================================
Author: Ramsey (Rayla) Phuc
Alias: Rayla Kurosaki
GitHub: https://github.com/rkp1503
Project: Red Blood Cell Production
=============================================================================#

module phase3
    using Plots

    export solve_model
    function solve_model(model, R₀, M₀, γₛ, tₘₐₓ)
        Rₛ = zeros((length(γₛ), tₘₐₓ + 1))
        Mₛ = zeros((length(γₛ), tₘₐₓ + 1))
        tₛ = LinRange(0, tₘₐₓ, tₘₐₓ + 1)
        for (i₁, γ) in enumerate(γₛ)
            Rₛᵢ = Rₛ[i₁, :]
            Mₛᵢ = Mₛ[i₁, :]
            Rₛᵢ[1] = R₀
            Mₛᵢ[1] = M₀
            for t in 1:tₘₐₓ
                Rₛᵢ, Mₛᵢ = model([Rₛᵢ, Mₛᵢ], γ, t)
            end
            Rₛ[i₁, :] = Rₛᵢ
            Mₛ[i₁, :] = Mₛᵢ
        end
        return tₛ, Rₛ, Mₛ
    end;

    export myPlot
    function myPlot(tₛ, Rₛ, γₛ, filename, colors, normalize=1)
        figure = Plots.plot(
            title="Red Blood Cell Population over $(length(tₛ) - 1) Days", 
            xaxis="Time in days", 
            yaxis="Percentage of Red Blood Cell Population", 
            legend=:outertopright,  
            foreground_color_grid="#000000", 
            gridalpha=1, 
            gridlinewidth=:1.5, 
            minorgrid=true, 
            foreground_color_minor_grid=:"#FF0000", 
            minorgridalpha=0.75
            )
        # Graph the solutions to the proposed model.
        for (i, (γ, color)) in enumerate(zip(γₛ, colors))
            Plots.plot!(
                figure, tₛ, Rₛ'[:, i]/normalize, label="γ=$γ", linecolor=color, 
                linewidth=2
                )
        end
        # Display the figure.
        return figure
    end;
end
