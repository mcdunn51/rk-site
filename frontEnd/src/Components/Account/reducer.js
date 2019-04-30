const accountsReducer = (state=[], action) => {
    switch(action.type) {
        case 'LOAD_MAIN_ACCOUNT_DETAILS':
            return action.payload

        default:
            return state
    }
}

export default accountsReducer