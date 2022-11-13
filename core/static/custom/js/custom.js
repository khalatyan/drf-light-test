function toggle(event) {
  var myCollapse = document.getElementsByClassName('collapse')[0];
  var bsCollapse = new bootstrap.Collapse(myCollapse, {
    toggle: true
  });
}