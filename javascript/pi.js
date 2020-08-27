// 1.假设一个半径为R的圆
// 2.以圆的半径画一个正方形
// 3.圆的四分之一处于这个正方形内
// 4.在正方形内随机生成n个点，计算处于圆中的点出现的概率

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

