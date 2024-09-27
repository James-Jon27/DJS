const IMAGE_COMMENTS = "image/comments";
const ADD_COMMENT = `comments/add`;
const DEL_COMMENT = `comments/delete`;

const imageComments = (comments) => {
	return {
		type: IMAGE_COMMENTS,
		payload: comments,
	};
};

const addComment = (comment) => {
	return {
		type: ADD_COMMENT,
		payload: comment,
	};
};

const delComm = (commentId) => {
	return {
		type: DEL_COMMENT,
		payload: commentId,
	};
};

export const getImageComments = (id) => async (dispatch) => {
	const res = await fetch(`/api/images/${id}/comments`);
	const data = await res.json();
	dispatch(imageComments(data));
};

export const postComment = (imageId, comment) => async (dispatch) => {
	const res = await fetch(`/api/images/${imageId}/new_comment`, {
		method: "POST",
		body: comment,
	});
	const data = await res.json();
	dispatch(addComment(data));
	return data;
};

export const deleteComment = (commentId) => async (dispatch) => {
	try {
		const res = await fetch(`/api/comments/${commentId}`, {
			method: "DELETE",
		});
		const data = await res.json();

		if (!res.ok) {
			throw new Error(data.errors || "Failed to delete comment");
		}

		dispatch(delComm(data)); 
		return data; 
	} catch (error) {
		console.error("Error deleting comment:", error);
		throw error;
	}
};

const initialState = {};

function commentReducer(state = initialState, action) {
	switch (action.type) {
		case IMAGE_COMMENTS:
			return action.payload;
		case ADD_COMMENT: {
			const ap = action.payload;
			const newState = { ...state };
			newState[ap.id] = action.payload;
			return newState;
		}
		case DEL_COMMENT: {
			const newState = { ...state };
			delete newState[action.payload];
			return newState;
		}
		default:
			return state;
	}
}

export default commentReducer;
