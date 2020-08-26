package leetcode

//leetcode17 电话号码的字母组合
//解法：深度优先搜索

var phoneMap map[string]string = map[string]string{
	"2": "abc",
	"3": "def",
	"4": "ghi",
	"5": "jkl",
	"6": "mno",
	"7": "pqrs",
	"8": "tuv",
	"9": "wxyz",
}
var res []string

func letterCombinations(digists string) []string{
	if digists == ""{
		return []string{}
	}
	res = []string{}
	backtrack(digists,0,"")
	return res
}

func backtrack(digists string,index int,s string){
	if index == len(digists){
		res = append(res,s)
	}else {
		num := string(digists[index])
		letter := phoneMap[num]
		for i := 0;i < len(letter);i++{
			backtrack(digists,index+1,s+string(letter[i]))
		}
	}
}
