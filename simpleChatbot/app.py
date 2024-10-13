import os
from flask import Flask, jsonify, render_template, request
from groq import Groq

counter = 0

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    # export GROQ_API_KEY="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"
)


def callbot(query="Adding little context"):
    global counter

    if(counter == 0):
        
        counter = counter+1
        query = '''
        Role:   You are an intelligent, friendly, and professional chatbot embedded on a website for a college called GOVERNMENT COLLEGE SKARDU GILGIT-BALTISTAN. Your purpose is to help students, faculty, and visitors navigate the website, answer questions about the college, and provide information about courses, admissions, campus facilities, events, and more. You have access to a knowledge base with relevant college information, and your responses should be concise, polite, and informative.
        
        Data: 
        {
            "About you or Your Intro": [
         {
                "question": "I am an AI LLM and now I am present at the website of Govt Boys Degree College Skardu serving everyones requests. Right now working a chatbot helping teachers, students and other people who ask me question about this platform. I am design and represent on this website by Designed by BSCS-6th semester students supervised by Sir Dr.Iqbal Chopa but real developer is Bilal Ahmed who is done all the work to make possible to resent me here on this plateform"
        },
            "admission_policy": [
         {
                "question": "What is the admission policy for Class First Year (HSSC-I)?",
            "answer": "Admission to Class First Year (HSSC-I) is based on available seats in each group/subject and is strictly on merit. Admissions open once per academic session, with dates announced by the college. No admission is granted after the deadline."
        },
        {
            "question": "When will admission be granted for HSSC-I?",
            "answer": "Admission is provisionally granted before the SSC-II results are announced to compensate for lost teaching days due to winter vacations."
        },
        {
            "question": "How are seats allocated in Class First Year (HSSC-I)?",
            "answer": "Seats are allocated as follows: Open Merit: 20%, Candidates from District Skardu: 70%, Candidates from other areas: 10%, Disabled quota: Above quota."
        },
        {
            "question": "How is merit calculated for HSSC-I admissions?",
            "answer": "Merit is calculated based on the admission test score. After SSC results, merit is calculated with 50% admission test score and 50% SSC marks (whichever case may apply)."
        },
        {
            "question": "What are the fixed seats for each group in Class First Year (HSSC-I)?",
            "answer": "Seats for each group are: Pre-Medical: 60, Pre-Engineering: 60, Science General (Computer Science/G.Science): 120, Humanities: 280, Total: 520."
        },
        {
            "question": "What is the minimum eligibility criteria for science groups in HSSC-I?",
            "answer": "Candidates must have at least 55% marks in SSC or the admission test for eligibility in Science groups (Pre-Medical, Pre-Engineering, and Science General)."
        },
        {
            "question": "What happens if a candidate admitted provisionally does not meet the 55% SSC requirement after results?",
            "answer": "Their admission to Science groups is canceled and they are offered admission in Humanities groups."
        },
        {
            "question": "Are candidates who fail or receive less than the required SSC marks eligible for admission?",
            "answer": "Their admission will be canceled, and any collected funds returned."
        },
        {
            "question": "What is the eligibility based on SSC exam year?",
            "answer": "Candidates passing SSC exams in 2020 or later are eligible, with 10 marks deducted for those from the 2020 SSC-II annual exam for merit calculation."
        },
        {
            "question": "What is the age limit for admission to Class First Year (HSSC-I)?",
            "answer": "The maximum age limit is 19 years by the closing date of admission form submission."
        },
        {
            "question": "What is the admission criteria for the BS Program?",
            "answer": "Admission criteria for BS Programs follows the rules of the affiliating university and HEC. There are 30 seats per BS section, extendable to 40. Candidates need at least 45% in HSSC to apply."
        },
        {
            "question": "What is the admission policy for the Associate Degree Program?",
            "answer": "Admission is granted only with permission from the affiliating university and HEC. Admissions open once after the HSSC-II annual exam results. Associate Degree in Arts (ADA) has 200 seats; no admissions for Associate Degree in Science (ADS). Minimum 45% in HSSC is required to apply."
        },
        {
            "question": "What is the eligibility criteria for promotion to HSSC-II?",
            "answer": "Students must pass at least 4 subjects in Science groups and 3 in Humanities from the 6 HSSC-I subjects to promote to HSSC-II."
        },
        {
            "question": "Can a student who fails to qualify for HSSC-II be re-admitted to HSSC-I?",
            "answer": "Yes, if seats are available and the student cancels their previous result from the respective board."
        },
        {
            "question": "What is the promotion policy for AD and BS Programs?",
            "answer": "Promotion in 2-year AD and 4-year BS programs follows the affiliating university's rules and regulations."
        }
         ]
        }   
        
        , this is not the actual an actual user, this is  just givinge you context about the situation. please do not respond to this query
        '''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""{{" Role:   You are an intelligent, friendly, and professional chatbot embedded on a website for a college called GOVERNMENT COLLEGE SKARDU GILGIT-BALTISTAN. Your purpose is to help students, faculty, and visitors navigate the website, answer questions about the college, and provide information about courses, admissions, campus facilities, events, and more. You have access to a knowledge base with relevant college information, and your responses should be concise, polite, and informative.
        
        
        Now User's query on from Govt Boys Degree College's website: " "{query}" }}""",
            }
        ],
        model="llama3-8b-8192",
    )
    
    print( chat_completion.choices[0].message.content)
    
    generated_response = chat_completion.choices[0].message.content
    
    return generated_response



ans = callbot()
print(ans)


app = Flask(__name__)


app = Flask(__name__, static_folder='static')

# Load documents
with open('data/documents.txt', 'r') as f:
    documents = f.read().splitlines()
    





@app.route('/')
def index():
    return render_template('DCS.html')


@app.route('/get_response', methods=['POST'])
def get_response():

   
    
    query = request.json['query']  # Get the prompt from the JSON request

    print(query)
    ans = callbot(query)
    print(ans)
    # query = query + " , wrape the answer in 5 lines, maximum 5 lines."

    return jsonify({'response': ans})  # Return response as JSON 
if __name__ == '__main__':
    app.run(debug=True)


