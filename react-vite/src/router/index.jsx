import { createBrowserRouter } from "react-router-dom";
import {
	UserProfileLayout,
	UserProfilePostedImage,
	UserProfileStash,
} from "../components/UserProfilePage";
import HomePage from "../components/HomePage";
import ExplorePage from "../components/ExplorePage/ExplorePage";
import UploadImagePage from "../components/UploadImagePage";
import Layout from "./Layout";
import StashPage from '../components/StashPage'
import UploadStash from "../components/UploadStash";
import UpdateImage from "../components/UploadImagePage/UpdateImage";
import UpdateStash from "../components/UploadStash/UpdateStash";
import FavoritesPage from "../components/StashPage/FavoritesPage";

export const router = createBrowserRouter([
	{
		element: <Layout />,
		children: [
			{
				path: "/",
				element: <HomePage />,
			},
			{
				path: "explore",
				element: <ExplorePage />
			},
			{
				path: "user/:userId",
				element: <UserProfileLayout />,
				children: [
					{
					path: "posted-images",
					element: <UserProfilePostedImage />
					},
					{
					path: "stashes",
					element: <UserProfileStash />
					},
				]
			},
			{
				path: "user/:userId/favorites",
				element: <FavoritesPage />
			},
			{
				path: "images/new",
				element: <UploadImagePage />
			},
			{
				path: "images/:id/edit",
				element: <UpdateImage />
			},
			{
				path: "stashes/new",
				element: <UploadStash />
			}, 
			{
				path: "stashes/:id",
				element: <StashPage />
			},
			{
				path: "stashes/:id/edit",
				element: <UpdateStash />
			},
			{
				path: "*",
				element: "Page Not Found",
			},
		],
	},
]);
