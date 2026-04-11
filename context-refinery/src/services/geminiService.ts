import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY || '' });

export async function distillContent(content: string): Promise<string> {
  if (!process.env.GEMINI_API_KEY) {
    return "Gemini API key not configured. Please add it to your secrets.";
  }

  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-flash-preview",
      contents: `Summarize the following content in exactly 3 sentences for use in a RAG embedding index. Focus on semantic core concepts:\n\n${content}`,
    });

    return response.text || "Failed to generate summary.";
  } catch (error) {
    console.error("Gemini Error:", error);
    return "Error distilling content.";
  }
}
