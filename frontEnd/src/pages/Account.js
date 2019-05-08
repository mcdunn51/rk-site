import React from 'react'
import Index from '../Components/Account'

const Account = (props) => {
    return (
        <Index id={props.match.params.id}/>
    )
}

export default Account;