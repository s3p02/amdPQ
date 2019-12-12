package stringManipulation

class charCount(var strChar: Char, var strCharCount: Int = 0)

object strMan {

  def verifyCount(count:Int):Int={
    if (count <= 9){
      println(s"OBJECT strMan - METHOD verifyCount - count:$count")
      count
    }
    else {
      println("OBJECT strMan - METHOD verifyCount - count:9")
      9
    }
  }

  def checkAndReturn(icc:charCount):String={
    if(icc.strCharCount <= 2){
      val returnResult = icc.strChar+icc.strChar.toString()
      println(s"OBJECT strMan - METHOD checkAndReturn - returnResult:$returnResult")
      returnResult
    }
    else{
      val returnResult = "z"+icc.strChar+verifyCount(icc.strCharCount)
      println(s"OBJECT strMan - METHOD checkAndReturn - returnResult:$returnResult")
      returnResult
    }
  }

  def strManip(inputString:String):String={
    var cache:String = ""
    var prevChar = new charCount(inputString(0),1)
    for(i <- 1 until inputString.length-1){
      println(s"OBJECT strMan - METHOD strManip - iteration:$i")
      var curChar = inputString(i)
      if(curChar == prevChar.strChar) {
        prevChar.strCharCount += 1
      }
      else{
        cache += checkAndReturn(prevChar)
        prevChar = new charCount(inputString(i),1)
      }
    }
    cache += checkAndReturn(prevChar)
    cache
  }

  def main(args: Array[String]): Unit = {
    val inputString:String = "aabbbccccdddddeeeeeefffffffgggggggghhhhhhhhhiiiiiiiiii"
    println(s"OBJECT strMan - METHOD main - INPUT:$inputString")
    val result = strManip(inputString)
    println(s"OBJECT strMan - METHOD main - OUTPUT:$result")
  }
}