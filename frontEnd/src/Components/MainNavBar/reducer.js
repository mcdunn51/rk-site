export const brandsReducer = (state = [], action) => {
    switch (action.type) {
        case 'LOAD_BRANDS':
            return action.payload

        default:
            return state

    }
}

export const electricalsReducer = (state = [], action) => {
    switch (action.type) {
        case 'LOAD_ELECTRICALS':
            return action.payload

        default:
            return state
    }
}

export const housewaresReducer = (state = [], action) => {
    switch (action.type) {
        case 'LOAD_HOUSEWARES':
            return action.payload

        default:
            return state
    }
}






