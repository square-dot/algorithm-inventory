include("Location.jl")


function kmeans(locations::Vector{Location}, k::Int64)
    throw("unimplemented")
end

function val(lsts)
    throw("unimplemented")
end


function repeatkmeans(locations, k, n)
    res_0 = kmeans(locations, k)
    for _ in 1:(n-1)
        res = kmeans(locations, k)
        if val(res_0) > val(res)
            res_0 = res
        end
    end
    return res_0
end