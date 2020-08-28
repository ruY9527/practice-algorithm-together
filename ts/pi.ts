// 计算圆周率（近似）


const R: number = 100

interface Point{
    x: number,
    y: number
}

function point(): Point {
    const x: number = Math.random() * R
    const y: number = Math.random() * R
    return {x, y}
}

function isCircleArea(point: Point): Boolean {
    const { x, y } = point
    return Math.sqrt(x*x + y*y) < R
}

function Pi(n: number = 100000000): Number {
    let circleAreaPoint: number = 0
    for (let i = 0; i < n; i++) {
        const p: Point = point()
        if (isCircleArea(p)) {
            circleAreaPoint++
        }
    }
    return (circleAreaPoint / n) * 4
}

console.log(Pi())

