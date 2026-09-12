### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    match question:
        case "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
            answer = "pcap"
        case "Are encoding and encryption the same? - Yes/No":
            answer = "No"
        case "Is it possible to decrypt a message without a key? - Yes/No":
            answer = "No"
        case "Is it possible to decode a message without a key? - Yes/No":
            answer = "Yes"
        case "Is a hashed message supposed to be un-hashed? - Yes/No":
            answer = "No"
        case "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
            answer = "282c8ac09290df385fcbb63ff74d9d41057ec8214657b4c588b3a447c434e561"
        case "Is MD5 a secured hashing algorithm? - Yes/No":
            answer = "No"
        case "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
            answer = 5
        case "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
            answer = 3
        case _:
            # Catch unrecognized questions, including typos.
            answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
