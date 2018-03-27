
function startup(){
    if(screen.width<=600){



    console.log("startup code running");

    //calling creatingHeading1 function
    createHeading1("Hello World");

    //calling creatingHeading2 function
    createHeading2("Hello World");
  }
  else{

    //calling creatingHeading3 function
    createHeading3("Hello World");

    //calling createParagraph function
    createParagraph();
  }
}

/* creating function createheading for H1  */
function createHeading1(titleText){

    //creating h1 element
    var heading1 = document.createElement("h1");
    //creating text for heading
    var text = document.createTextNode(titleText);
    //appending element to body
    document.body.appendChild(heading1);
    //appending text to h1
    heading1.appendChild(text);
}

/* creating function createheading for H2  */
function createHeading2(titleText){

    //creating h2 element
    var heading2 = document.createElement("h2");
    //creating text for heading
    var text = document.createTextNode(titleText);
    //appending element to body
    document.body.appendChild(heading2);
    //appending text to h2
    heading2.appendChild(text);
}

/* creating function createheading for H3  */
function createHeading3(titleText){

    //creating h3 element
    var heading3 = document.createElement("h3");
    //creating text for heading
    var text = document.createTextNode(titleText);
    //appending element to body
    document.body.appendChild(heading3);
    //appending text to h3
    heading3.appendChild(text);
}

/* creating function createParagraph  */
function createParagraph(){

    //creating paraghraph element
    var paragraph = document.createElement("p");
    //creating text for paragraph
    var text = document.createTextNode("This is my paragraph");
    //appending element to body
    document.body.appendChild(paragraph);
    //appending text to paragraph
    paragraph.appendChild(text);
}
window.onload = startup;
