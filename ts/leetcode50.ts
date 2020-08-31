// pown

function myPow(x: number, n: number): number {
    if (n === 0) return 1
    if (n === 1) return x
    if (n === -1) return 1 / x
    const a: number = myPow(x, ~~(n / 2))
    const b: number = myPow(x, (n % 2))
    return a * a * b
}

console.log(myPow(2, -2))