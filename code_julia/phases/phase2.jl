#=============================================================================
Author: Ramsey (Rayla) Phuc
Alias: Rayla Kurosaki
GitHub: https://github.com/rkp1503
Project: Red Blood Cell Production
=============================================================================#

module phase2
using DifferentialEquations: ODEProblem, solve

    function solve_model(model, vars_dict, params_dict, days)
        initial_vector = collect(values(vars_dict))
        parameter_values = collect(values(params_dict))
        t_span = (0, days)
        problem = DifferentialEquations.ODEProblem(
            model, initial_vector, t_span, parameter_values
            )
        return DifferentialEquations.solve(problem, reltol=1e-8, abstol=1e-8)
    end;
    
end
