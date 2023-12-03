// First Question 
let answer_holder = document.getElementById("answer-holder")
let question_holder = document.getElementById("question-holder")

question_holder.addEventListener('click',()=>{
    answer_holder.classList.toggle('answer-holder')
})


// Second Question
let second_question = document.getElementById("question-holder-2")
let second_answer = document.getElementById("answer-holder-2")

second_question.addEventListener('click',()=>{
   second_answer.classList.toggle("answer-holder")
})

// Third quetsion 
let third_question = document.getElementById("question-holder-3")
let third_answer = document.getElementById("answer-holder-3")
third_question.addEventListener('click',()=>{
    third_answer.classList.toggle('answer-holder')
})

// fourth question 
let fourth_question = document.getElementById("question-holder-4")
let fourth_answer = document.getElementById("answer-holder-4")

fourth_question.addEventListener("click",()=>{
    fourth_answer.classList.toggle("answer-holder")
})
