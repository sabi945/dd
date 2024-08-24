function factorial(n)
    if n == 0
        return 1
    else
        return n * factorial(n - 1)
    end
end

# Contoh penggunaan
number = 5
result = factorial(number)
println("Faktorial dari ", number, " adalah ", result)
