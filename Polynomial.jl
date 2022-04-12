using Test

struct Polynomial
    coefficients::Array
end


function Base.:*(poly1::Polynomial, poly2::Polynomial)
    cf = zeros(1, length(poly1.coefficients) + length(poly2.coefficients) - 1)
    for (index, value) in enumerate(poly1.coefficients)
        for (i, v) in enumerate(poly2.coefficients)
            cf[index + i - 1] += value * v
        end
    end
    return Polynomial(cf)
end



@test (Polynomial([1, 2])*Polynomial([1, 2])).coefficients == [1 4 4]
