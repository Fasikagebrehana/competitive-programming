func luckyNumbers (matrix [][]int) []int {
    n := len(matrix)
    m := len(matrix[0])
    mininRow := make([]int, n)
    maxinCol := make([]int, m)
    var lucky []int 
    for i := 0; i < n; i++{
        minn := 1000000
        for j := 0; j < m; j++{
            if minn > matrix[i][j]{
                minn = matrix[i][j]
            }
        }
        mininRow[i] = minn
    }

    for i := 0; i < m; i++{
        maxx := 0
        for j := 0; j < n; j++{
            if maxx < matrix[j][i]{
                maxx = matrix[j][i]
            }
        }
        maxinCol[i] = maxx
    }

    for _, num := range mininRow{
        for _, maxNum := range maxinCol {
            if num == maxNum{
                lucky = append(lucky, num)
            }
        }
    }

    return lucky
}