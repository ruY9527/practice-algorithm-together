// 计算圆周率（近似）


const R = 100

function point() {
    const x = Math.random() * R
    const y = Math.random() * R
    return {x, y}
}

function isCircleArea(point) {
    const { x, y } = point
    return Math.sqrt(x*x + y*y) < R
}

function Pi(n) {
    let circleAreaPoint = 0
    for (let i = 0; i < n; i++) {
        const p = point()
        if (isCircleArea(p)) {
            circleAreaPoint++
        }
    }
    return (circleAreaPoint / n) * 4
}

console.log(Pi(100000000))

