document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;

    $.get(url, function (data, textStatus) {
      if (textStatus === 'success') {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
