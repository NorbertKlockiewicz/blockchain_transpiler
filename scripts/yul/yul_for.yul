function factorial(n) -> result, habla {
    result := 1
    habla := 2
    for { let i := 1 } lt(i, n) { i := add(i, 1) } {
        result := mul(result, i)
    }
}

function fibonacci(n: u256, k: u256, j) -> result: u256 {
    let fib := 0
    let prevFib := 1

    for { let i := 0 } lt(i, n) { i := add(1, i) } {
        let temp := fib
        fib := add(fib, prevFib)
        prevFib := temp
    }

    result := fib
}

function fac() -> result {
    result := factorial(5)
}
