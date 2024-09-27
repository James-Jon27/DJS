const GET_SEARCH_LABEL = 'get/search-label'

export const getSearchLabel = (label) => {
    return {
        type: GET_SEARCH_LABEL,
        payload: label
    }
}

function searchLabelReducer(state = "", action) {
    switch(action.type){
        case GET_SEARCH_LABEL:
            return action.payload
        default:
            return state
    }
}

export default searchLabelReducer