#=============================================================================
Author: Ramsey (Rayla) Phuc
Alias: Rayla Kurosaki
GitHub: https://github.com/rkp1503
Project: Red Blood Cell Production
=============================================================================#

module phase2
    using DifferentialEquations
    using Plots

    export solve_model
    function solve_model(model_to_solve, vars_dict, params_dict, days)
        # Get the values of the initial populations as a vector.
        initial_vector = collect(values(vars_dict))
        # Get the values of the parameters as a vector.
        parameter_values = collect(values(params_dict))
        # Initialize a period of time to solve the model over.
        t_span = (0, days)
        # Construct the problem to solve.
        problem = DifferentialEquations.ODEProblem(
            model_to_solve, initial_vector, t_span, parameter_values
            )
        # Numerically solve the proposed model.
        solutions = DifferentialEquations.solve(
            problem, reltol=1e-8, abstol=1e-8
            )
    end;
    
    export myPlot
    function myPlot(t_arr, R_arr, γₛ, filename, colors, normalize=1)
        num_days = (trunc(Int, last(t_arr[1]) - t_arr[1][1]))
        figure = Plots.plot(
            title="Red Blood Cell Population over $num_days Days", 
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
        for (tₛ, Rₛ, label, color) in zip(t_arr, R_arr, γₛ, colors)
            Plots.plot!(
                figure, tₛ, Rₛ/normalize, label=label, linecolor=color, 
                linewidth=2
                )
        end
        # Display the figure.
        return figure
    end;
end
