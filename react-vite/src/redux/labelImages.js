const GET_MATCH = "images/getImages";

const getImgs = (images) => ({
	type: GET_MATCH,
	payload: images,
});

export const imageByLabel = (label) => async (dispatch) => {
	const res = await fetch(`/api/images/${label}`);
	const data = await res.json();
	dispatch(getImgs(data));
};

export default function labelImageReducer(state = {}, action) {
	switch (action.type) {
		case GET_MATCH: {
			const newState = { ...action.payload };
			return newState;
		}
		default:
			return state;
	}
}
