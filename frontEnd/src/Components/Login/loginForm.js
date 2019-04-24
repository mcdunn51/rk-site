import React from 'react'
import { Field, reduxForm } from 'redux-form'
import {Button} from 'react-bootstrap';

let LoginForm = props => {
    const { handleSubmit } = props
    return (
        <form onSubmit={handleSubmit} className="form">
            <div className="form-group">
                <label htmlFor="username" className="form-label">USERNAME</label>
                <Field name="username" component="input" type="text" className="form-control" required />
            </div>
            <div className="form-group">
                <label htmlFor="Password" className="form-label">PASSWORD</label>
                <Field name="pwd" component="input" type="password" className="form-control" required />
            </div>
            <div id="pwdWrapper">
                <a id="forgottenPwd">Forgotten Password?</a>
            </div>
            <Button type="submit">SIGN IN</Button>
        </form>
    )
}

LoginForm = reduxForm({
    form: 'login'
})(LoginForm)


export default LoginForm; 