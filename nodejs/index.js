const express = require('express')
const body_parser = require('body-parser')
const cors = require('cors')
const app = express()

//definir como se quiere tratamiento urls
app.use(body_parser.urlencoded({extended: true}))
app.use(body_parser.json())
app.use(cors())


const db_manager = require('./persistence/dbmanager')

/*app.get('/', (req, res)=>{
    res.send('API REST Curso')
})*/

app.get('/', (req, res) =>{
    res.send({
        'name': 'Dario',
        'age': 15
    })
})

//CRUD
//C CREATE - POST
app.post('/user', (req, res) =>{
    db_manager.user_create(req, res)
})

//R READ - GET
app.get('/user', (req, res) =>{
    db_manager.user_details(req, res)
})

//U UPDATE - PUT/PATCH
app.put('/user', (req, res) =>{
    db_manager.user_update(req, res)
})

//D DELETE - DELETE
app.delete('/user', (req, res) =>{
    db_manager.user_delete(req, res)
})

app.listen(8082, () => {
    console.log('API REST running in port 8082!')
})