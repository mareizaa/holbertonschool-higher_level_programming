const $ = window.$;
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (response) {
    $('#character').text(response.name);
  }
});
