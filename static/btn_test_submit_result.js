
// document.getElementById("clickMe").onclick = SendTestResult;





document.getElementById("process_test_result").addEventListener("submit", function (e) {
    e.preventDefault();

    form = document.getElementById("process_test_result");
    formData = new FormData(form);
    var testAnswers = new Object();
    
    for (var key_value of formData.entries()) {

        testAnswers[String(key_value[1].split("_")[0])] = Number(key_value[1].split("_")[1]);
    }

    // document.getElementById("test_result_printed").innerHTML = testAnswers;
    console.log(testAnswers);
  });
  
