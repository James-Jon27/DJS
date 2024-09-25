const GET_LABELS = 'get/labels'

const getLabels = (labels) => {
    return {
        type: GET_LABELS,
        payload: labels
    }
}

export const getLabelsForExplore = () => async (dispatch) =>{
    const res = await fetch(`/api/images/labels`)
    const data = await res.json()
    dispatch(getLabels(data))
}

function labelReducer(state = {}, action) {
    switch(action.type){
        case GET_LABELS:
            return action.payload
        default:
            return state
    }
}

export default labelReducer