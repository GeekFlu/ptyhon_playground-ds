def reverse_string(input_str):
    """
    Return reversed input string
    Examples:
       reverse_string("abc") returns "cba"
    Args:
      input_str(str): string to be reversed
    Returns:
      a string that is the reverse of input
    """
    if len(input_str) == 0:
        return ""
    else:
        first_char = input_str[0]
        the_rest = input_str[1:len(input_str)]
        reversed_str = reverse_string(the_rest)
        return reversed_str + first_char


"""
This does not work on python
JAVA CODE
@Slf4j
public class ReverseString {
  public static String reverse(String inputStr) {
    if (Objects.isNull(inputStr) || inputStr.length() == 0) {
      return null;
    } else {
      int i = 0;
      int j = inputStr.length() - 1;
      char[] cad = inputStr.toCharArray();
      while (i < j){
        char temp = cad[i];
        cad[i] = cad[j];
        cad[j] = temp;
        i++;
        j--;
      }
      return new String(cad);
    }
  }
"""


def reverse_string_iterative(input_str):
    if input_str is None or len(input_str) == 0:
        return None
    else:
        p1_string = ""
        p2_string = ""
        i = 0
        j = len(input_str) - 1
        while i < j:
            temp = input_str[i]
            p1_string += input_str[j]
            p2_string += temp
            i += 1
            j -= 1
        return p1_string + p2_string


if __name__ == "__main__":
    print("Pass" if ("siul" == reverse_string_iterative("luis")) else "Fail")
    print("Pass" if ("anitalavalatina" == reverse_string("anitalavalatina")) else "Fail")
    print("Pass" if ("siul" == reverse_string("luis")) else "Fail")
    print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
    print("Pass" if ("" == reverse_string("")) else "Fail")
