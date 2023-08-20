import React, {useState} from "react"
import { Form, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import { useForm } from 'react-hook-form'

const SignUpPage = () => {

    const {register, watch, handleSubmit, reset, formState: { errors }} = useForm();

    const SubmitForm = (data) => {
       
        console.log(data)
        reset()
    }

    console.log(watch("username"))
    console.log(watch("email"))
    console.log(watch("password"))
    console.log(watch("confirmPassword"))

    return(
        <div className="container">
            <div className="form">
                <h1>SignUp</h1>
                <form>
                    <Form.Group>
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text" placeholder="Your username"
                                      {...register("username", {required:true, maxLength:25})} />
                    </Form.Group>
                    {errors.username && <span style={{color:"red"}}>Username is required</span>}
                    <br></br> 
                    <Form.Group>
                        <Form.Label>Email</Form.Label>
                        <Form.Control type="email" placeholder="Your email"
                                      {...register("email", {required:true, maxLength:80})} />
                    </Form.Group>
                    <br></br>
                    <Form.Group>
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Your password"
                                      {...register("password", {required:true, minLength:8})} />
                    </Form.Group>
                    <br></br>
                    <Form.Group>
                        <Form.Label>Confirm Password</Form.Label>
                        <Form.Control type="password" placeholder="Your password"
                                      {...register("confirmPassword", {required:true, minLength:8})}/>
                    </Form.Group>
                    <div className="submit-button">
                        <Form.Group>
                            <Button as="sub" variant="outline-success" onClick={handleSubmit(SubmitForm)}>SignUp</Button>
                        </Form.Group>
                    </div>
                    <div className="end-notes">
                        <Form.Group>
                            <small> Already have an account? <Link to='/login'> Login </Link></small>
                        </Form.Group>      
                    </div>
                </form>
            </div>
        </div>
    )
}

export default SignUpPage