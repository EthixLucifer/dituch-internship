import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";
const TOKEN = "eafd7ca342f109191535a27954497703d5c4e02d";

const axiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    Authorization: `Token ${TOKEN}`,
    "Content-Type": "application/json",
  },
});

export const fetchEntries = async (date = "") => {
  try {
    const response = await axiosInstance.get(`/entries/${date ? `?date=${date}` : ""}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching entries:", error.response?.data || error);
    return [];
  }
};

export const clockIn = async () => {
  try {
    await axiosInstance.post("/entries/", {
      project: 1,
      activity: 1,
      location: 1,
      status: 1,
    });
  } catch (error) {
    console.error("Error clocking in:", error.response?.data || error);
  }
};

export const clockOut = async (id) => {
  try {
    await axiosInstance.put(`/entries/${id}/`, { end_time: new Date().toISOString() });
  } catch (error) {
    console.error("Error clocking out:", error.response?.data || error);
  }
};

export const fetchDailyEntries = async (date) => {
  try {
    const response = await axiosInstance.get(`/entries/?date=${date}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching entries:", error);
    return [];
  }
};

export const fetchWeeklyEntries = async (startDate) => {
  try {
    const response = await axiosInstance.get(`/entries/?start_date=${startDate}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching weekly entries:", error);
    return [];
  }
};