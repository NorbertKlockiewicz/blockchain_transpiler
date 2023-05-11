function factorial(n) -> result {
    result := 1
    for { let i := 1 } lt(i, n) { i := add(i, 1) } {
        result := mul(result, i)
    }
}

function fibonacci(n: u256) -> result: u256 {
    let fib := 0
    let prevFib := 1

    for { let i := 0 } lt(i, n) { i := add(i, 1) } {
        let temp := fib
        fib := add(fib, prevFib)
        prevFib := temp
    }

    result := fib
}
