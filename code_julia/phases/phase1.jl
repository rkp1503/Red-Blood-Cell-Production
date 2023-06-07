#=============================================================================
Author: Ramsey (Rayla) Phuc
Alias: Rayla Kurosaki
GitHub: https://github.com/rkp1503
Project: Red Blood Cell Production
=============================================================================#

module phase1

    function solve_model(model, R₀, M₀, f, γₛ, tₘₐₓ)
        Rₛ = zeros((length(γₛ), tₘₐₓ + 1))
        Mₛ = zeros((length(γₛ), tₘₐₓ + 1))
        tₛ = LinRange(0, tₘₐₓ, tₘₐₓ + 1)
        for (i₁, γ) in enumerate(γₛ)
            Rₛᵢ = Rₛ[i₁, :]
            Mₛᵢ = Mₛ[i₁, :]
            Rₛᵢ[1] = R₀
            Mₛᵢ[1] = M₀
            for t in 1:tₘₐₓ
                Rₛᵢ, Mₛᵢ = model([Rₛᵢ, Mₛᵢ], [f, γ], t)
            end
            Rₛ[i₁, :] = Rₛᵢ
            Mₛ[i₁, :] = Mₛᵢ
        end
        return tₛ, Rₛ, Mₛ
    end;
    
end
