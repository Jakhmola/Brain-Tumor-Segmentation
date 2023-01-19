function myFunc() {
  var slider = document.getElementById("myRange");
  var output = document.getElementById("rangeValue");
  var image = document.getElementById("img");
  output.innerHTML = slider.value;
  var n_slice = 'prediction'+String(slider.value-1)+'.png'
  image.src = "http://127.0.0.1:5000/uploads/"+n_slice
}