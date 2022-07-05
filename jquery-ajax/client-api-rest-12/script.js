$('#guarda_usuario').click(function(){
    var name = $('#name').val()
    var age = $('#age').val()
    var data_user = { 'name': name, 'age': age }

    $.ajax({
        type: 'POST',
        url: 'http://localhost:8082/user',
        contentType: 'application/json',
        data: JSON.stringify(data_user)
    }).done(function(){
        alert('User saved')
    }).fail(function(err){
        alert(err)
    })
})

$('#obtener_usuario').click(function(){
    var id = $('#id').val()

    fetch('http://localhost:8082/user?id=' + id)
        .then(response => response.json())
        .then(data => alert(JSON.stringify(data)))
})