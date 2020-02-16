$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  for (let movie = 0; movie < data.results.length; movie++) {
    $('UL#list_movies').append('<li>' + data.results[movie].title + '</li>');
  }
});
