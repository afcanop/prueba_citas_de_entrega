export const setItemLocalStorage = (key: string, value: string) => {
    if (typeof window !== "undefined") {
        localStorage.setItem(key, value);
    }
};

export const getItemLocalStorage = (key: string): string | null => {
    if (typeof window !== "undefined") {
        return localStorage.getItem(key);
    }
    return null;
}