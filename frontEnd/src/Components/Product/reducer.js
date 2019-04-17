const productDetailedReducer = (state=[], action) => {
    switch(action.type) {
        case 'LOAD_DETAILED_PRODUCT':
            return action.payload

        default:
            return state
    }
}

export default productDetailedReducer